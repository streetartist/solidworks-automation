# InsertChainDimensions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertChainDimensions`

Chains dimensions for the specified entities in this drawing or sketch.
Chains dimensions for the specified entities in this drawing or sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertChainDimensions( _
   ByVal Entities As System.Object _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Entities As System.Object
Dim value As System.Object
 
value = instance.InsertChainDimensions(Entities)
```

```

System.object InsertChainDimensions( 
   System.object Entities
)
```

```

System.Object^ InsertChainDimensions( 
   System.Object^ Entities
) 
```

#### Parameters

*Entities*
:   Array of entities, e.g., edges, vertices, circles, and midpoints with which to chain dimensions (see **Remarks**)

#### Return Value

Array of [IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)s

Remarks

The first element in Entities is the starting entity which is used to dimension the second element. The second element is used to dimension the third element, and so on. If Entities is Nothing or null, then pre-selected entities are used to create the chain dimensions.

The array of chain dimensions returned contains one fewer element than the array of Entities.

For more information, see the **SOLIDWORKS help > Detailing and Drawings > Drawings > Dimensions in Drawings > Chain Dimensions** topic.

Example

'VBA

' Preconditions:

' 1. Open *install\_dir***\samples\tutorial\advdrawings\foodprocessor.slddrw**.  
' 2. Select the **Sheet2** tab at the bottom.  
' 3. Open the Immediate window.  
'  
' Postconditions:  
' 1. Observe the chained dimensions in **Drawing View3**.  
' 2. Inspect the display dimensions in the Immediate window.

Option Explicit  
  
Dim swApp As SldWorks.SldWorks  
Dim modDocExt As SldWorks.ModelDocExtension  
Dim Part As SldWorks.ModelDoc2  
Dim selectMgr As SldWorks.SelectionMgr  
Dim dimArray As Variant  
Dim entityArray(3) As Object  
Dim varArray As Variant  
Dim myDisplayDim As SldWorks.DisplayDimension  
Dim swDim As SldWorks.Dimension  
Dim dimText As String  
Dim k As Integer  
Dim boolstatus As Boolean

Sub main()

    Set swApp = Application.SldWorks  
    Set Part = swApp.ActiveDoc  
    Set selectMgr = Part.SelectionManager  
    Set modDocExt = Part.Extension  
     
    Part.ClearSelection2 True  
    boolstatus = Part.ActivateView("Drawing View3")  
    boolstatus = Part.Extension.SelectByRay(0.107406727925462, 0.259964392021715, 375.00575, 0, 0, -1, 1.93314752083778E-03, 1, False, 0, 0)  
    Set entityArray(0) = selectMgr.GetSelectedObject6(1, -1)  
     
    boolstatus = Part.Extension.SelectByRay(0.135835367937783, 0.281001585630832, 375.00575, 0, 0, -1, 1.93314752083778E-03, 1, False, 0, 0)  
    Set entityArray(1) = selectMgr.GetSelectedObject6(2, -1)  
     
    boolstatus = Part.Extension.SelectByRay(0.140383950339754, 0.25598438241999, 375.00575, 0, 0, -1, 1.93314752083778E-03, 1, False, 0, 0)  
    Set entityArray(2) = selectMgr.GetSelectedObject6(3, -1)

    boolstatus = Part.Extension.SelectByRay(0.176772609555524, 0.221301441604959, 375.00275, 0, 0, -1, 1.93314752083778E-03, 1, False, 0, 0)  
    Set entityArray(3) = selectMgr.GetSelectedObject6(4, -1)  
     
    varArray = entityArray  
    
    dimArray = modDocExt.**InsertChainDimensions**(varArray)

    If Not IsEmpty(dimArray) Then  
        For k = 0 To UBound(dimArray)  
            Set myDisplayDim = dimArray(k)  
            Set swDim = myDisplayDim.GetDimension2(0)  
            dimText = swDim.Value  
            Debug.Print dimText  
        Next k  
    End If  
   
End Sub

Example

[Insert Chain Dimensions (VB.NET)](Insert_Chain_Dimensions_Example_VBNET.htm)  
[Insert Chain Dimensions (C#)](Insert_Chain_Dimensions_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
