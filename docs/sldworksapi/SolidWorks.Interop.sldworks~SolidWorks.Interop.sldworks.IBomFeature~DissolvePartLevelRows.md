# DissolvePartLevelRows Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DissolvePartLevelRows`

Gets or sets whether to dissolve weldment part level rows.
Gets or sets whether to dissolve weldment part level rows.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DissolvePartLevelRows As System.Boolean
```

```

Dim instance As IBomFeature
Dim value As System.Boolean
 
instance.DissolvePartLevelRows = value
 
value = instance.DissolvePartLevelRows
```

```

System.bool DissolvePartLevelRows {get; set;}
```

```

property System.bool DissolvePartLevelRows {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to dissolve component rows, false to not

Remarks

This getter of this property is valid only when [IBomFeature::DetailedCutList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DetailedCutList.md) is set to true.

The setter of this property is valid only for:

- BOM tables of type [swBomType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomType_e.html).swBomType\_Indented (call [IBomFeature::TableType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~TableType.md) to get the BOM table type)

    - and -

- when IBomFeature::DetailedCutList is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)
