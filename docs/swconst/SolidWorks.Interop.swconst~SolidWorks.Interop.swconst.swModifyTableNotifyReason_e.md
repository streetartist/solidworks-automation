# swModifyTableNotifyReason_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swModifyTableNotifyReason_e`

Notification reason codes for modifying tables.
Notification reason codes for modifying tables.

Syntax

- [Visual Basic](#Syntax-VBAll)
- [C#](#Syntax-CS)
- [Delphi](#Syntax-Delphi)
- [JScript](#Syntax-JScript)
- [Managed Extensions for C++](#Syntax-CPP)
- [C++/CLI](#Syntax-CPP2005)

```

'Declaration
 
```

```

<System.Runtime.InteropServices.GuidAttribute("D5A30E7A-8520-464A-B0D1-6AD4D22B374D")>
Public Enum swModifyTableNotifyReason_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swModifyTableNotifyReason_e
```

```

[System.Runtime.InteropServices.Guid("D5A30E7A-8520-464A-B0D1-6AD4D22B374D")]
public enum swModifyTableNotifyReason_e : System.Enum 
```

```

public enum swModifyTableNotifyReason_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("D5A30E7A-8520-464A-B0D1-6AD4D22B374D")
public enum swModifyTableNotifyReason_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("D5A30E7A-8520-464A-B0D1-6AD4D22B374D")]
__value public enum swModifyTableNotifyReason_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("D5A30E7A-8520-464A-B0D1-6AD4D22B374D")]
public enum class swModifyTableNotifyReason_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swModifyTableNotifyReason\_CellDataModify** | 7 |
| **swModifyTableNotifyReason\_CellMerge** | 9 |
| **swModifyTableNotifyReason\_CellUnMerge** | 10 |
| **swModifyTableNotifyReason\_ColumnDeletion** | 6 |
| **swModifyTableNotifyReason\_ColumnInsertionLeft** | 0 |
| **swModifyTableNotifyReason\_ColumnInsertionRight** | 1 |
| **swModifyTableNotifyReason\_ColumnPropertyModify** | 8 |
| **swModifyTableNotifyReason\_ColumnRellocation** | 4 |
| **swModifyTableNotifyReason\_CustomPropertyModify** | 12 |
| **swModifyTableNotifyReason\_EditMultiProp** | 11 |
| **swModifyTableNotifyReason\_RowInsertionAbove** | 2 |
| **swModifyTableNotifyReason\_RowInsertionBelow** | 3 |
| **swModifyTableNotifyReason\_RowRellocation** | 5 |
| **swModifyTableNotifyReason\_TableMerge** | 17 |
| **swModifyTableNotifyReason\_TableSplitHorizontallyAbove** | 15 |
| **swModifyTableNotifyReason\_TableSplitHorizontallyBelow** | 16 |
| **swModifyTableNotifyReason\_TableSplitVerticallyLeft** | 13 |
| **swModifyTableNotifyReason\_TableSplitVerticallyRight** | 14 |

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swModifyTableNotifyReason\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
