# CombineSameSize Property (IHoleTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineSameSize`

Gets or sets whether to merge cells of the same size in this hole table.
Gets or sets whether to merge cells of the same size in this hole table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CombineSameSize As System.Boolean
```

```

Dim instance As IHoleTable
Dim value As System.Boolean
 
instance.CombineSameSize = value
 
value = instance.CombineSameSize
```

```

System.bool CombineSameSize {get; set;}
```

```

property System.bool CombineSameSize {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to merge cells of the same size, false to not

Remarks

This property appears in the Scheme section of the Hole Table PropertyManager page in SOLIDWORKS.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md)  
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.md)  
[IHoleTable::CombineTags Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineTags.md)  
[IHoleTable::ShowANSIInchLetterNumberDrillSizes Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~ShowANSIInchLetterNumberDrillSizes.md)
