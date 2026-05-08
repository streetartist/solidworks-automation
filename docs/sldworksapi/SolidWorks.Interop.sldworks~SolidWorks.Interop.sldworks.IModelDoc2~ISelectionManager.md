# ISelectionManager Property (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISelectionManager`

Gets the ISelectionMgr object for this document, which makes the currently selected object available.
Gets the [ISelectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md) object for this document, which makes the currently selected object available.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ISelectionManager As SelectionMgr
```

```

Dim instance As IModelDoc2
Dim value As SelectionMgr
 
value = instance.ISelectionManager
```

```

SelectionMgr ISelectionManager {get;}
```

```

property SelectionMgr^ ISelectionManager {
   SelectionMgr^ get();
}
```

#### Property Value

[ISelectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md) object

Remarks

[ISelectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md) objects are transient because they are invalid as soon as another selection is made. So, do not hold on to these pointers for any length of time.

Example

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)  
[Deselect Every Other Selected Object (C++)](Deselect_Every_Other_Selected_Object_Example_CPlusPlus_COM.htm)  
[Display of Item in FeatureManager Design Tree (C++)](Display_of_Item_in_Feature_Manager_Example_CPlusPlus_COM.htm)  
[Get Curve Spline Points (C++)](Get_Curve_Spline_Points_Example_CPlusPlus_COM.htm)  
[Get Parent Features (C++)](Get_Parent_Features_Example_CPlusPlus_COM.htm)  
[Get Selected Feature (C++)](Get_Selected_Feature_Example_CPlusPlus_COM.htm)  
[Get Sketch Segment Constraints (C++)](Get_Sketch_Segment_Constraints_Example_CPlusPlus_COM.htm)  
[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SelectionManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectionManager.md)
