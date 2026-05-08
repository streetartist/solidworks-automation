# GetComponentRep Method (ISwDMTable)

Help ID: `SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetComponentRep`
![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

|  |  |
| --- | --- |
| SOLIDWORKS Document Manager API Help | [Send comments](mailto:apihelp.feedback@3ds.com?subject=Documentation Feedback: SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetComponentRep.html) on this topic. |
| GetComponentRep Method (ISwDMTable) | |
| [See Also](#seealsobookmark) | |

|  |
| --- |
| Collapse All  Expand All   Language Filter: All Language Filter: Multiple Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C# Language Filter: C++/CLI |

|  |
| --- |
| [SolidWorks.Interop.swdocumentmgr Namespace](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr_namespace.md) > [ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md) : GetComponentRep Method (ISwDMTable) |

Visual Basic (Declaration)
  

Visual Basic (Usage)
  

C#
  

C++/CLI

*RowIndex*
:   Row number for the component representation

*ComponentRep*
:   Component representation

Gets the component representation.

# .NET Syntax

| Visual Basic (Declaration) |  |
| --- | --- |
| ``` Function GetComponentRep( _    ByVal RowIndex As System.Integer, _    ByRef ComponentRep As System.String _ ) As SwDmTableError ``` | |

| Visual Basic (Usage) | Copy Code |
| --- | --- |
| ``` Dim instance As ISwDMTable Dim RowIndex As System.Integer Dim ComponentRep As System.String Dim value As SwDmTableError   value = instance.GetComponentRep(RowIndex, ComponentRep) ``` | |

| C# |  |
| --- | --- |
| ``` SwDmTableError GetComponentRep(     System.int RowIndex,    out System.string ComponentRep ) ``` | |

| C++/CLI |  |
| --- | --- |
| ``` SwDmTableError GetComponentRep(  &   System.int RowIndex, &   [Out] System.String^ ComponentRep ) ``` | |

#### Parameters

*RowIndex*
:   Row number for the component representation

*ComponentRep*
:   Component representation

#### Return Value

Error as defined in [SwDmTableError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDmTableError.md)

# Visual Basic for Applications (VBA) Syntax

See [SwDMTable::GetComponentRep](swdocumentmgr~SwDMTable~GetComponentRep.md).

# Remarks

Before calling this method, call [ISwDMTable::GetRowCount](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable~GetRowCount.md) to determine the index of the row for the component representation.

# See Also

#### 

[ISwDMTable Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable.md)
  
[ISwDMTable Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMTable_members.md)

# Availability

SOLIDWORKS Document Manager API 2009 SP0
