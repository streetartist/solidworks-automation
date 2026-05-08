# CombineTags Property (IHoleTable)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineTags`

Gets or sets whether to combine tags for same-size holes.
Gets or sets whether to combine tags for same-size holes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CombineTags As System.Boolean
```

```

Dim instance As IHoleTable
Dim value As System.Boolean
 
instance.CombineTags = value
 
value = instance.CombineTags
```

```

System.bool CombineTags {get; set;}
```

```

property System.bool CombineTags {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to combine tags for same-size holes, false to not

Remarks

This property appears in the Scheme section of the Hole Table PropertyManager page in SOLIDWORKS.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md)  
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.md)  
[IHoleTable::HoleTag Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTag.md)  
[IHoleTable::HoleTagsVisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleTagsVisible.md)  
[IHoleTable::TagStyle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~TagStyle.md)  
[IHoleTable::CombineSameSize Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineSameSize.md)  
[IHoleTable::ShowANSIInchLetterNumberDrillSizes Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~ShowANSIInchLetterNumberDrillSizes.md)
