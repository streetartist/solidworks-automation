# AutoSpaceBodiesOnDrag Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep~AutoSpaceBodiesOnDrag`

Gets or sets whether to automatically space a group of bodies equally along an axis as you drag them in this explode step.
Gets or sets whether to automatically space a group of bodies equally along an axis as you drag them in this explode step.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AutoSpaceBodiesOnDrag As System.Boolean
```

```

Dim instance As IPartExplodeStep
Dim value As System.Boolean
 
instance.AutoSpaceBodiesOnDrag = value
 
value = instance.AutoSpaceBodiesOnDrag
```

```

System.bool AutoSpaceBodiesOnDrag {get; set;}
```

```

property System.bool AutoSpaceBodiesOnDrag {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to automatically space components equally along an axis as you drag them, false to not

Example

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.md)  
[IPartExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.md)
