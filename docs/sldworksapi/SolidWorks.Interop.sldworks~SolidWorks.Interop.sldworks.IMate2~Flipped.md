# Flipped Property (IMate2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Flipped`

Gets or sets whether to flip the distance or angle mate.
Gets or sets whether to flip the distance or angle mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Flipped As System.Boolean
```

```

Dim instance As IMate2
Dim value As System.Boolean
 
instance.Flipped = value
 
value = instance.Flipped
```

```

System.bool Flipped {get; set;}
```

```

property System.bool Flipped {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the mate, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::CanBeFlipped Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~CanBeFlipped.md)  
[IMate2::Type Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~Type.md)
