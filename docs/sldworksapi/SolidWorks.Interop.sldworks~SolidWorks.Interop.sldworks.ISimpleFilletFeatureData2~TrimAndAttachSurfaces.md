# TrimAndAttachSurfaces Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~TrimAndAttachSurfaces`

Gets or sets the Trim surfaces option for surface face fillets.
Gets or sets the Trim surfaces option for surface face fillets.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TrimAndAttachSurfaces As System.Integer
```

```

Dim instance As ISimpleFilletFeatureData2
Dim value As System.Integer
 
instance.TrimAndAttachSurfaces = value
 
value = instance.TrimAndAttachSurfaces
```

```

System.int TrimAndAttachSurfaces {get; set;}
```

```

property System.int TrimAndAttachSurfaces {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

- 0 = Trim and attach (trims the filleted face and knits the surfaces into one surface body)

- 1 = Don't trim or attach (adds a new fillet surface, but does not trim the faces or knit the surfaces)

- -1 = Not applicable

Example

See [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)
