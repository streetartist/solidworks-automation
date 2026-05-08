# DisplayTitle Property (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~DisplayTitle`

Gets this component's title as displayed in the FeatureManager design tree.
Gets this component's title as displayed in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property DisplayTitle As System.String
```

```

Dim instance As IComponent2
Dim value As System.String
 
value = instance.DisplayTitle
```

```

System.string DisplayTitle {get;}
```

```

property System.String^ DisplayTitle {
   System.String^ get();
}
```

#### Property Value

Display title

Remarks

To get and set the display title of an assembly, drawing or part, use [IModelDocExtension::DisplayTitle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayTitle.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
