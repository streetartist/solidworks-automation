# EnableAssemblyRebuild Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EnableAssemblyRebuild`

Gets or sets whether to suspend the rebuild of the assembly.
Gets or sets whether to suspend the rebuild of the assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnableAssemblyRebuild As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim value As System.Boolean
 
instance.EnableAssemblyRebuild = value
 
value = instance.EnableAssemblyRebuild
```

```

System.bool EnableAssemblyRebuild {get; set;}
```

```

property System.bool EnableAssemblyRebuild {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to suspend rebuilding the assembly, false to rebuild the assembly (false is the default)

Example

[Suspend Automatic Rebuilds (VBA)](Suspend_Automatic_Rebuilds_of_an_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
