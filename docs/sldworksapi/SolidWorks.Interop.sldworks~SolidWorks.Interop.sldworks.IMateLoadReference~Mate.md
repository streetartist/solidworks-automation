# Mate Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~Mate`

Gets the mate that owns this mate load reference.
Gets the mate that owns this mate load reference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Mate As Mate2
```

```

Dim instance As IMateLoadReference
Dim value As Mate2
 
value = instance.Mate
```

```

Mate2 Mate {get;}
```

```

property Mate2^ Mate {
   Mate2^ get();
}
```

#### Property Value

[Mate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md) that owns this mate load reference

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.md)  
[IMateLoadReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference_members.md)
