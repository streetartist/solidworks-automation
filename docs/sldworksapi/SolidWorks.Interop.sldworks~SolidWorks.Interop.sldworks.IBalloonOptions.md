# IBalloonOptions Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions`

Allows access to balloon options.
Allows access to balloon options.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IBalloonOptions 
```

```

Dim instance As IBalloonOptions
```

```

public interface IBalloonOptions 
```

```

public interface class IBalloonOptions 
```

Remarks

To create a BOM balloon:

1. Select an item for which to create a BOM balloon.
2. Call [IModelDocExtension::CreateBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateBalloonOptions.md) to create an IBalloonOptions object.
3. Set the properties on the IBalloonOptions object.
4. Pass the IBalloonOptions object in a call to [IModelDocExtension::InsertBOMBalloon2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2.md).

Example

'VBA

'This example demonstrates how to get the balloon options for a ballooned note in a drawing.

'-----------------------------------------------------------------------  
' Preconditions:  
' 1. Open any SOLIDWORKS drawing containing a ballooned note.  
' 2. Select a balloon.  
' 3. Open an Immediate window.  
'  
'Postconditions: Inspect the Immediate window.  
'-----------------------------------------------------------------------

Dim swApp As SldWorks.SldWorks  
Dim swModel As SldWorks.ModelDoc2

Option Explicit

Sub main()

    Set swApp = Application.SldWorks  
    Set swModel = swApp.ActiveDoc  
     
    Dim selMgr As SldWorks.SelectionMgr  
    Set selMgr = swModel.SelectionManager  
     
    Dim Note1 As SldWorks.Note  
    Set Note1 = selMgr.GetSelectedObject6(1, -1)  
     
    Dim balloonOptions As SldWorks.balloonOptions  
    Set balloonOptions = Note1.**GetBalloonOptions**()  
     
    Debug.Print "Balloon Options"  
    Debug.Print ""  
     
    Debug.Print "Custom size: " & balloonOptions.CustomSize  
    Debug.Print "Size as defined by swBalloonFit\_e: " & balloonOptions.Size  
    Debug.Print "Style as defined by swBalloonStyle\_e: " & balloonOptions.Style  
     
    Debug.Print "Upper text: " & balloonOptions.UpperText  
    Debug.Print "Upper text style as defined by swBalloonTextContent\_e: " & balloonOptions.UpperTextContent  
     
    Debug.Print "Lower text: " & balloonOptions.LowerText  
    Debug.Print "Lower text style as defined by swBalloonTextContent\_e: " & balloonOptions.LowerTextContent  
     
    Debug.Print "Item quantity label: " & balloonOptions.QuantityDenotationText  
    Debug.Print "Override the item quantity? " & balloonOptions.QuantityOverride  
    Debug.Print "Override item quantity value: " & balloonOptions.QuantityOverrideValue  
    Debug.Print "Placement of the item quantity as defined by swBalloonQuantityPlacement\_e"; " & balloonOptions.QuantityPlacement"  
    Debug.Print "Display the item quantity? " & balloonOptions.ShowQuantity  
     
    ' Item-related options are valid only for drawings and need to be extracted from linked BOM feature instead of from IBalloonOptions (see below)  
    'Debug.Print "Item number increment from IBalloonOptions: " & balloonOptions.ItemNumberIncrement  
    'Debug.Print "Item nuumber start from  IBalloonOptions:" & balloonOptions.ItemNumberStart  
    'Debug.Print "Item order from IBalloonOptions: " & balloonOptions.ItemOrder  
     
    ' Layername option is valid only for drawings; empty string for parts and assemblies; empty string for drawings where the layer name is -None-  
    Debug.Print "Layer name: " & balloonOptions.Layername  
     
    ' Item-related options are valid only for drawings  
    If (swModel.GetType() = swDocDRAWING) Then  
     
        Dim swDraw As SldWorks.DrawingDoc  
        Set swDraw = swModel  
         
        Dim annot As SldWorks.Annotation  
        Set annot = Note1.GetAnnotation()  
         
        Dim view1 As SldWorks.View  
        Set view1 = annot.Owner  
         
        Dim bomTableName1 As String  
        bomTableName1 = view1.GetKeepLinkedToBOMName()  
         
        If bomTableName1 = "" Then  
         
            Debug.Print "No BOM table, no item-related properties"  
             
        Else  
            Dim Feat1 As SldWorks.Feature  
            Set Feat1 = swDraw.FeatureByName(bomTableName1)  
             
            Debug.Print "BOM table name: " & bomTableName1  
             
            Dim bomFeat As SldWorks.BomFeature  
            Set bomFeat = Feat1.GetSpecificFeature2()  
             
            Debug.Print "Keep current BOM item numbers: " & bomFeat.KeepCurrentItemNumbers  
            Debug.Print "Follow assembly item order: " & bomFeat.FollowAssemblyOrder2  
            Debug.Print "Item start number: " & bomFeat.SequenceStartNumber  
        End If  
     
    End If

End Sub

Example

[Insert and Show BOM Table and BOM Balloon (VBA)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VB.htm)  
[Insert and Show BOM Table and BOM Balloon (VB.NET)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VBNET.htm)  
[Insert and Show BOM Table and BOM Balloon (C#)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md)  
[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md)
