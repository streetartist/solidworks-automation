# GetCreateFeatureErrors Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetCreateFeatureErrors`

Gets the errors that occurred during the last call to IFeatureManager::CreateFeature.
Gets the errors that occurred during the last call to [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCreateFeatureErrors( _
   ByRef Msgs As System.Object, _
   ByRef FeatureTypeName As System.String _
) As System.Integer
```

```

Dim instance As IFeatureManager
Dim Msgs As System.Object
Dim FeatureTypeName As System.String
Dim value As System.Integer
 
value = instance.GetCreateFeatureErrors(Msgs, FeatureTypeName)
```

```

System.int GetCreateFeatureErrors( 
   out System.object Msgs,
   out System.string FeatureTypeName
)
```

```

System.int GetCreateFeatureErrors( 
   [Out] System.Object^ Msgs,
   [Out] System.String^ FeatureTypeName
) 
```

#### Parameters

*Msgs*
:   Array of errors as defined by [swCreateFeatureError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCreateFeatureError_e.html)

*FeatureTypeName*
:   Feature type name

#### Return Value

0 <= Number of messages issued at the time of last call to IFeatureManager::CreateFeature <= 20

Remarks

This method is valid only after attempting to create [Mate Controller](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md) features using IFeatureManager::CreateFeature.

Example

'VBA

' ===============================================  
' Preconditions:  
' 1. Open *Public\_documents***\SOLIDWORKS\SOLIDWORKS 2024\samples\tutorial\api\AdvancedMates\advancedmatedemo1.sldasm**.  
' 2. Create two distance mates to center the steel disc inside the magnet.  
'  
' Postconditions:  
' 1. Inspect the Immediate window.  
' 2. Mate controller feature is not created.  
' 3. Observe the returned error code: 6 indicates that the number of mate selections (2)  
'    do not match the number of values (3) in the specified position data array.  
' ========================================================  
Dim swApp As SldWorks.SldWorks  
Dim Part As SldWorks.ModelDoc2  
Dim Assem As SldWorks.AssemblyDoc  
Dim boolstatus As Boolean  
Dim i As Long, j As Long, longstatus As Long, longwarnings As Long  
Option Explicit

Sub main()

    Set swApp = Application.SldWorks  
     
    Set Part = swApp.ActiveDoc  
    Set Assem = Part  
     
    Dim myModelView As Object  
    Set myModelView = Part.ActiveView  
    myModelView.FrameState = swWindowState\_e.swWindowMaximized  
    Part.ClearSelection2 True  
     
    Dim var As Variant  
    var = Assem.**CollectAllSupportiveMates**  
     
    Debug.Print "Mates:"  
    For i = 0 To UBound(var)  
        var(i).Select2 True, 0  
        Debug.Print "  " & var(i).Name  
    Next  
     
    Dim featMgr As SldWorks.FeatureManager  
    Set featMgr = Part.FeatureManager  
     
    Dim mateControllerObj As MateControllerFeatureData  
    Set mateControllerObj = featMgr.**CreateDefinition**(swFmMateController)  
     
    mateControllerObj.**AddNewPosition** ("Position1")  
    mateControllerObj.**AddNewPosition** ("Position2")  
    mateControllerObj.**AddNewPosition** ("Position3")  
     
    Dim position2ValArr(2) As Double  
    position2ValArr(0) = 1.0646  
    position2ValArr(1) = 0.0635  
    position2ValArr(2) = 1.02  
     
    Call mateControllerObj.**SetValues**("Position2", position2ValArr)  
     
    Dim posVar As Variant  
    Dim valArr As Variant  
    posVar = mateControllerObj.**GetPositions**()  
    valArr = mateControllerObj.**GetValues**("Position3")  
     
    Dim position3ValArr(2) As Double  
    position3ValArr(0) = 1#  
    position3ValArr(1) = 0.0635  
    position3ValArr(2) = 1.05  
     
    Call mateControllerObj.**SetValues**("Position3", position3ValArr)  
     
    mateControllerObj.**AddConfigurationFromPosition** "Position 2", False  
     
    mateControllerObj.**DeletePosition** ("Position 1")  
     
    Dim posArr(2) As String  
    posArr(0) = "Position3"  
    posArr(1) = "Position2"  
    posArr(2) = "Position1"  
     
    mateControllerObj.**ReOrderPositions** ((posArr))  
     
    Dim mateContFeat As SldWorks.Feature  
    Set mateContFeat = featMgr.**CreateFeature**(mateControllerObj)  
    Dim err As Variant  
    Dim FeatureType As String  
    Dim cnt As Long  
    cnt = featMgr.**GetCreateFeatureErrors**(err, FeatureType)  
    Debug.Print "Number of errors returned: " & cnt  
    Debug.Print "Feature type: " & FeatureType  
     
    For j = 0 To UBound(err)  
        Debug.Print "Error code as defined by swCreateFeatureError\_e: " & err(j)  
    Next

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
