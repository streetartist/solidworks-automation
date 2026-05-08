# UpdateProgress Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar~UpdateProgress`

Increments the progress indicator.
Increments the progress indicator.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UpdateProgress( _
   ByVal Position As System.Integer _
) As System.Integer
```

```

Dim instance As IUserProgressBar
Dim Position As System.Integer
Dim value As System.Integer
 
value = instance.UpdateProgress(Position)
```

```

System.int UpdateProgress( 
   System.int Position
)
```

```

System.int UpdateProgress( 
   System.int Position
) 
```

#### Parameters

*Position*
:   New position of the progress indicator

#### Return Value

Status of progress indicator update as defined in [swUpdateProgressError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUpdateProgressError_e.html)

Example

See the [IUserProgressBar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserProgressBar Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.md)  
[IUserProgressBar Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar_members.md)
