# TableTypeID Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable~TableTypeID`

Gets the fastener table type ID associated with this Hole Wizard fastener table.
Gets the fastener table type ID associated with this Hole Wizard fastener table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property TableTypeID As System.Integer
```

```

Dim instance As IHoleDataTable
Dim value As System.Integer
 
value = instance.TableTypeID
```

```

System.int TableTypeID {get;}
```

```

property System.int TableTypeID {
   System.int get();
}
```

#### Property Value

Fastener table type ID as defined in [swFastenerTableTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFastenerTableTypes_e.html)

Example

See the [IHoleDataTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleDataTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable.md)  
[IHoleDataTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable_members.md)
