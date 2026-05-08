# SeparateRequirement Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SeparateRequirement`

Gets or sets whether a SEP REQT label is present with the Gtol symbol.
Gets or sets whether a SEP REQT label is present with the Gtol symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SeparateRequirement As System.Boolean
```

```

Dim instance As IGtol
Dim value As System.Boolean
 
instance.SeparateRequirement = value
 
value = instance.SeparateRequirement
```

```

System.bool SeparateRequirement {get; set;}
```

```

property System.bool SeparateRequirement {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if a SEP REQT label is present, false if not

Remarks

The Separate Requirement label is present below the Gtol frame.

Example

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)
