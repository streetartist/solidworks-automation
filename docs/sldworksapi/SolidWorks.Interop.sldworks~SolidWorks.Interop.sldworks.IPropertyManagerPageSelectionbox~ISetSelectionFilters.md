# ISetSelectionFilters Method (IPropertyManagerPageSelectionbox)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~ISetSelectionFilters`

Defines the types of objects the user can select for this selection box.
Defines the types of objects the user can select for this selection box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetSelectionFilters( _
   ByVal FilterCount As System.Short, _
   ByRef Filters As System.Integer _
) 
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim FilterCount As System.Short
Dim Filters As System.Integer
 
instance.ISetSelectionFilters(FilterCount, Filters)
```

```

void ISetSelectionFilters( 
   System.short FilterCount,
   ref System.int Filters
)
```

```

void ISetSelectionFilters( 
   System.short FilterCount,
   System.int% Filters
) 
```

#### Parameters

*FilterCount*
:   Number of filters

*Filters*
:   - in-procses, unmanaged C++: Array of filter values as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)  (see **Remarks**)

    VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md) and [IPropertyManagerPage2::Close](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md).

When a user makes a selection in the graphics area, SOLIDWORKS must decide whether to select a face, body, or component. The following table shows what appears in a selection box created with the specifed filters after a selection occurs in the graphics area.

|  |  |
| --- | --- |
| **Filters** | **Result** |
| swSelFACES,  swSelSOLIDBODIES | Face  If you want a body to appear in the selection box, then use swSelSOLIDBODIESFIRST. |
| swSelFACES, swSelCOMPONENTS | Component  If you want a face to appear in the selection box, then use swSELCOMPSDONTOVERRIDE. |
| swSelSOLIDBODIES, swSelCOMPONENTS | Component  If you want a body to appear in the selection box, then use swSelSOLIDBODIESFIRST. |
| swSelFACES, swSelSOLIDBODIES, swSelCOMPONENTS | Component  If you want a face to appear in the selection box, then use swSelCOMPSDONTOVERRIDE.  - or -  If you want a body to appear in the selection box, then use swSelSOLIDBODIESFIRST. |

swSelSURFACEBODIES and swSelSURFBODIESFIRST behave simliar to swSelSOLIDBODIES and swSelSOLIDBODIESFIRST. swSelEDGES and swSelVERTICES behave similar to swSelFACES. If the Filters is set to swSelNOTHING or swSelUNSUPPORTED, this the call to this method fails.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)
