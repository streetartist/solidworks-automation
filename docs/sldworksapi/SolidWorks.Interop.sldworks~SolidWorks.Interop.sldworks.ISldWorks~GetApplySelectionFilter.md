# GetApplySelectionFilter Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetApplySelectionFilter`

Gets the current state of the selection filter.
Gets the current state of the selection filter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetApplySelectionFilter() As System.Boolean
```

```

Dim instance As ISldWorks
Dim value As System.Boolean
 
value = instance.GetApplySelectionFilter()
```

```

System.bool GetApplySelectionFilter()
```

```

System.bool GetApplySelectionFilter(); 
```

#### Return Value

True if the selection filter is active, false if not

Remarks

If the selection filter is active, then the settings found in [ISldWorks::GetSelectionFilter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilter.md) and [ISldWorks::GetSelectionFilters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetSelectionFilters.md) or [ISldWorks::IGetSelectionFilters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFilters.md) apply.

|  |  |
| --- | --- |
| **Use...** | **To...** |
| ISldWorks::SetApplySelectionFilter | Activate or deactivate the selection filter |
| [ISldWorks::SetSelectionFilter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilter.md) and [ISldWorks::SetSelectionFilters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetSelectionFilters.md) or [ISldWorks::ISetSelectionFilters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ISetSelectionFilters.md) | Change the current filters in use |

Example

[Set and Toggle Selection Filters (VBA)](Clear,_Set,_and_Toggle_Selection_Filters_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::IGetSelectionFiltersCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetSelectionFiltersCount.md)  
[ISldWorks::SetApplySelectionFilter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetApplySelectionFilter.md)
