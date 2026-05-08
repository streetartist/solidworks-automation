# IGetExtent Method (IBomTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~IGetExtent`

Gets the lower-left and upper-right extents of the BOM on the drawing sheet.
Gets the lower-left and upper-right extents of the BOM on the drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetExtent() As System.Double
```

```

Dim instance As IBomTable
Dim value As System.Double
 
value = instance.IGetExtent()
```

```

System.double IGetExtent()
```

```

System.double IGetExtent(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

SOLIDWORKS returns the values in meters with respect to drawing sheet space.

The return value is the following array of doubles:

> **[** *lowerLeftPt[3], upperRightPt[3]* **]**

where:

- lowerLeftPt[3] is an array of 3 doubles describing the X,Y,Z location for the lower-left corner of the BOM
- upperRightPt[3] is an array of 3 doubles describing the X,Y,Z location for the upper-right corner of the BOM

Before you use any of the IBomTable methods, activate the BOM table using [IBomTable::Attach3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Attach3.md). After you finish getting BOM data, use [IBomTable::Detach](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~Detach.md) to deactivate the table.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable.md)  
[IBomTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.md)  
[IBomTable::GetExtent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable~GetExtent.md)
