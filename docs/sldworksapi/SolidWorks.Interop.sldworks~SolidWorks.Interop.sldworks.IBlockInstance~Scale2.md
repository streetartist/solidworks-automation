# Scale2 Property (IBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance~Scale2`

Obsolete. Superseded by ISketchBlockInstance::Scale.
Obsolete. Superseded by [ISketchBlockInstance::Scale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Scale.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Scale2 As System.Double
```

```

Dim instance As IBlockInstance
Dim value As System.Double
 
instance.Scale2 = value
 
value = instance.Scale2
```

```

System.double Scale2 {get; set;}
```

```

property System.double Scale2 {
   System.double get();
   void set (    System.double value);
}
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance.md)  
[IBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBlockInstance_members.md)
