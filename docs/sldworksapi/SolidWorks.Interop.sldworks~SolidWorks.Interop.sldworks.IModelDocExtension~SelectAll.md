# SelectAll Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll`

Selects all edges in a part, all components in an assembly, or all entities (by default, sketch entities, dimensions, and annotations) in a drawing.
Selects all edges in a part, all components in an assembly, or all entities (by default, sketch entities, dimensions, and annotations) in a drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SelectAll() 
```

```

Dim instance As IModelDocExtension
 
instance.SelectAll()
```

```

void SelectAll()
```

```

void SelectAll(); 
```

Remarks

This method behaves the same as box selecting everything in the graphics area of a part or assembly document or in a sheet of a drawing document.

To select entities different from the defaults, use selection filters. The **See Also** section contains links to methods related to selection filters.

Example

[Select All in Part, Assembly, or Drawing (C#)](Select_All_in_Part_Assembly_or_Drawing_Example_CSharp.htm)  
[Select All in Part, Assembly, or Drawing (VB.NET)](Select_All_in_Part_Assembly_or_Drawing_Example_vbnet.htm)  
[Select All in Part, Assembly, or Drawing (VBA)](Select_All_in_Part_Assembly_or_Drawing_Example_vb.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::MultiSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MultiSelect.md)  
[IModelDocExtension::IMultiSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IMultiSelect.md)  
[IModelDocExtension::SelectByID2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md)  
[IComponent2::Select4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select4.md)  
[IBody2::GetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetEdges.md)  
[IBody2::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetEdges.md)  
[IView::ISelectEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISelectEntity.md)  
[IView::SelectEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SelectEntity.md)  
[ISldWorks::GetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilter.md)  
[ISldWorks::GetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilters.md)  
[ISldWorks::IGetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFilters.md)  
[ISldWorks::IGetSelectionFiltersCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFiltersCount.md)  
[ISldWorks::ISetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetSelectionFilters.md)  
[ISldWorks::SetSelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilter.md)  
[ISldWorks::SetSelectionFilters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilters.md)  
[ISldWorks::GetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetApplySelectionFilter.md)  
[ISldWorks::SetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetApplySelectionFilter.md)  
[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md)  
[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[IAssemblyDoc::SelectComponentsBySize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectComponentsBySize.md)
