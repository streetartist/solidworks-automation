# InsertAlternateView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertAlternateView`

Inserts an Alternate Position View of the currently selected drawing view.
Inserts an **Alternate Position View** of the currently selected drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertAlternateView( _
   ByVal ConfigurationName As System.String _
) As View
```

```

Dim instance As IView
Dim ConfigurationName As System.String
Dim value As View
 
value = instance.InsertAlternateView(ConfigurationName)
```

```

View InsertAlternateView( 
   System.string ConfigurationName
)
```

```

View^ InsertAlternateView( 
   System.String^ ConfigurationName
) 
```

#### Parameters

*ConfigurationName*
:   Name of the configuration (see Remarks)

#### Return Value

Alternate [drawing view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)

Remarks

Before using this method, you must select a drawing view on which to superimpose the Alternate Position View.

If you specify a non-existent configuration for ConfigurationName, then it is created using all default settings. The new configuration is identical to the currently selected configuration. The user can then open the assembly, edit the configuration, and update the drawing view

Example

[Insert Alternate Position View (VBA)](Insert_Alternate_Position_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
