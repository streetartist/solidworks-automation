# SetName2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetName2`

Sets the name of this drawing view, as displayed in the FeatureManager design tree.
Sets the name of this drawing view, as displayed in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetName2( _
   ByVal Name As System.String _
) As System.Boolean
```

```

Dim instance As IView
Dim Name As System.String
Dim value As System.Boolean
 
value = instance.SetName2(Name)
```

```

System.bool SetName2( 
   System.string Name
)
```

```

System.bool SetName2( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Name of drawing view

#### Return Value

True if the name of the drawing view is set, false if not

Remarks

The drawing view name that you specify:

- must be unique in the FeatureManager design tree.
- not contain any of the SOLIDWORKS reserved special characters.

If either of these conditions is not met, then this method returns false and the name of the drawing view is not changed.

You cannot change the drawing view name for detail views and section views. If you attempt to do so, then false if returned and the drawing view name is not changed.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::GetName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetName2.md)
