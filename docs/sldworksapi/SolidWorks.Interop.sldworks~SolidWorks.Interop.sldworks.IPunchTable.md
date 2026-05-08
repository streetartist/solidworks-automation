# IPunchTable Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable`

Allows access to punch table information and values.
Allows access to punch table information and values.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IPunchTable 
```

```

Dim instance As IPunchTable
```

```

public interface IPunchTable 
```

```

public interface class IPunchTable 
```

Remarks

Punch tables contain information about the punches that are created by forming tools in sheet metal parts. A punch table contains the following information about pre-selected punches:

| Column | Description |
| --- | --- |
| TAG | Datum tag added to each punch in the flat pattern view |
| PUNCH ID | Property of the forming tool or library feature |
| X Location | Distance from the x-axis to the point of insertion of the forming tool in the flat pattern view |
| Y Location | Distance from the y-axis to the point of insertion of the forming tool in the flat pattern view |
| ANGLE | Angle between the x-axis and the forming tool |
| QUANTITY | Number of times that the forming tool is used in the flat pattern view |

Example

[Insert Punch Table (C#)](Insert_Punch_Table_Example_CSharp.htm)  
[Insert Punch Table (VB.NET)](Insert_Punch_Table_Example_VBNET.htm)  
[Insert Punch Table (VBA)](Insert_Punch_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPunchTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IPunchTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTableAnnotation.md)  
[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.md)
