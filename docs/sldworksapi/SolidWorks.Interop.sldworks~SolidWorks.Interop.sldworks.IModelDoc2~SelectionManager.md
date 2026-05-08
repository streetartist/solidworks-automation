# SelectionManager Property (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectionManager`

Gets the ISelectionMgr object for this document, which makes the currently selected object available.
Gets the [ISelectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md) object for this document, which makes the currently selected object available.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SelectionManager As System.Object
```

```

Dim instance As IModelDoc2
Dim value As System.Object
 
instance.SelectionManager = value
 
value = instance.SelectionManager
```

```

System.object SelectionManager {get; set;}
```

```

property System.Object^ SelectionManager {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

Remarks

[ISelectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md) objects are transient because they are invalid as soon as another selection is made. So, do not hold on to these pointers for any length of time.

Example

[Get Object's Persistent Reference ID (C++)](Get_Object_s_Persistent_Reference_ID_Example_CPlusPlus_COM.htm)  
[Create Plane Thru 3 Points In-context (VBA)](Create_Plane_Thru_3_Points_In-context_Example_VB.htm)  
[Determine If Sketch Suitable for Feature (VBA)](Determine_If_Sketch_Suitable_for_Feature_Example_VB.htm)  
[Find Total Length of Sketch Segments in Sketch (VBA)](Find_Total_Length_of_Sketch_Segments_in_Sketch_Example_VB.htm)  
[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)  
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)  
[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ISelectionManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISelectionManager.md)
