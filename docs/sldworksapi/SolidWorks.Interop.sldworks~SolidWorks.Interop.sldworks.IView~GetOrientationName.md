# GetOrientationName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetOrientationName`

Gets the predefined name of this view.
Gets the predefined name of this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOrientationName() As System.String
```

```

Dim instance As IView
Dim value As System.String
 
value = instance.GetOrientationName()
```

```

System.string GetOrientationName()
```

```

System.String^ GetOrientationName(); 
```

#### Return Value

Predefined name of view or an empty string for unnamed views

Remarks

This method returns the orientation (predefined) name of the view; e.g., \*Front, \*Top, \*Isometric, or a user-defined view name defined in the model. This method returns an empty string ("") for section views, detail views, projected views, and unfolded views.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
