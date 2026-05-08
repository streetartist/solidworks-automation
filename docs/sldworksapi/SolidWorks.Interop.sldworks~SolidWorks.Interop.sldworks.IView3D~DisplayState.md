# DisplayState Property (IView3D)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~DisplayState`

Gets or sets the name this 3D View's display state.
Gets or sets the name this 3D View's display state.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisplayState As System.String
```

```

Dim instance As IView3D
Dim value As System.String
 
instance.DisplayState = value
 
value = instance.DisplayState
```

```

System.string DisplayState {get; set;}
```

```

property System.String^ DisplayState {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Display state name

Example

See the [IView3D](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md)  
[IView3D Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.md)
