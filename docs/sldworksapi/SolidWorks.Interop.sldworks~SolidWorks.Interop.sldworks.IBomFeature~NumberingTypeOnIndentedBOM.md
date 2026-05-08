# NumberingTypeOnIndentedBOM Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~NumberingTypeOnIndentedBOM`

Gets and sets the type of numbering for this indented BOM table.
Gets and sets the type of numbering for this indented BOM table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NumberingTypeOnIndentedBOM As System.Integer
```

```

Dim instance As IBomFeature
Dim value As System.Integer
 
instance.NumberingTypeOnIndentedBOM = value
 
value = instance.NumberingTypeOnIndentedBOM
```

```

System.int NumberingTypeOnIndentedBOM {get; set;}
```

```

property System.int NumberingTypeOnIndentedBOM {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of numbering as defined in [swNumberingType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swNumberingType_e.html)

Example

See [IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)  
[IView::InsertBomTable4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable4.md)
