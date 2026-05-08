# ShowANSIInchLetterNumberDrillSizes Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~ShowANSIInchLetterNumberDrillSizes`

Gets or sets whether to display hole sizes in this hole table using ANSI inch letters and drill numbers.
Gets or sets whether to display hole sizes in this hole table using ANSI inch letters and drill numbers.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowANSIInchLetterNumberDrillSizes As System.Boolean
```

```

Dim instance As IHoleTable
Dim value As System.Boolean
 
instance.ShowANSIInchLetterNumberDrillSizes = value
 
value = instance.ShowANSIInchLetterNumberDrillSizes
```

```

System.bool ShowANSIInchLetterNumberDrillSizes {get; set;}
```

```

property System.bool ShowANSIInchLetterNumberDrillSizes {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display hole sizes using ANSI inch letters and drill numbers, false to not

Remarks

This property:

- corresponds to the **Show ANSI inch letter and number drill sizes** option in the Scheme section of the Hole Table PropertyManager page in SOLIDWORKS.
- is valid only for holes created with the Hole Wizard tool.
- specifies whether to display hole sizes as ANSI inch letters or drill numbers, for example, A or #40.

Example

[Get Labels of Datum Origin (VBA)](Get_Labels_of_Datum_Origin_Example_VB.htm)  
[Get Labels of Datum Origin (VB.NET)](Get_Labels_of_Datum_Origin_Example_VBNET.htm)  
[Get Labels of Datum Origin (C#)](Get_Labels_of_Datum_Origin_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md)  
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.md)  
[IHoleTable::CombineSameSize Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineSameSize.md)  
[IHoleTable::CombineTags Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~CombineTags.md)
