# MateLoadReference Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~MateLoadReference`

Gets the mate load reference associated with this mate.
Gets the mate load reference associated with this mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property MateLoadReference As MateLoadReference
```

```

Dim instance As IMate2
Dim value As MateLoadReference
 
value = instance.MateLoadReference
```

```

MateLoadReference MateLoadReference {get;}
```

```

property MateLoadReference^ MateLoadReference {
   MateLoadReference^ get();
}
```

#### Property Value

[Mate load reference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.md) for this mate, or Nothing or null if none exists

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)
