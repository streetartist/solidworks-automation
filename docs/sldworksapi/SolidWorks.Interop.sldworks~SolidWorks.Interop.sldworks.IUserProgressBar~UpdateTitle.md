# UpdateTitle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar~UpdateTitle`

Changes the title of the progress indicator.
Changes the title of the progress indicator.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UpdateTitle( _
   ByVal ProgressBarTitle As System.String _
) As System.Boolean
```

```

Dim instance As IUserProgressBar
Dim ProgressBarTitle As System.String
Dim value As System.Boolean
 
value = instance.UpdateTitle(ProgressBarTitle)
```

```

System.bool UpdateTitle( 
   System.string ProgressBarTitle
)
```

```

System.bool UpdateTitle( 
   System.String^ ProgressBarTitle
) 
```

#### Parameters

*ProgressBarTitle*
:   New title of progress indicator

#### Return Value

True if title successfully updated, false if not

Example

See the [IUserProgressBar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserProgressBar Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.md)  
[IUserProgressBar Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar_members.md)
