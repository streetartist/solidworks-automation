# IsSubAssemblyRigid Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~IsSubAssemblyRigid`

Gets whether the subassembly is rigid or flexible.
Gets whether the subassembly is rigid or flexible.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsSubAssemblyRigid() As System.Boolean
```

```

Dim instance As IExplodeStep
Dim value As System.Boolean
 
value = instance.IsSubAssemblyRigid()
```

```

System.bool IsSubAssemblyRigid()
```

```

System.bool IsSubAssemblyRigid(); 
```

#### Return Value

True if the subassembly is rigid, false if it is flexible

Remarks

See the SOLIDWORKS Help for more information about flexible and rigid subassemblies.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.md)  
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.md)  
[IComponent2::Solving Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Solving.md)
