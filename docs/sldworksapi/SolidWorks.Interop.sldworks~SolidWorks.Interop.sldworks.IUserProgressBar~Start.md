# Start Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar~Start`

Sets the range of the progress indicator display and shows it on the SOLIDWORKS status bar.
Sets the range of the progress indicator display and shows it on the SOLIDWORKS status bar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Start( _
   ByVal LowerBound As System.Integer, _
   ByVal UpperBound As System.Integer, _
   ByVal ProgressBarTitle As System.String _
) As System.Boolean
```

```

Dim instance As IUserProgressBar
Dim LowerBound As System.Integer
Dim UpperBound As System.Integer
Dim ProgressBarTitle As System.String
Dim value As System.Boolean
 
value = instance.Start(LowerBound, UpperBound, ProgressBarTitle)
```

```

System.bool Start( 
   System.int LowerBound,
   System.int UpperBound,
   System.string ProgressBarTitle
)
```

```

System.bool Start( 
   System.int LowerBound,
   System.int UpperBound,
   System.String^ ProgressBarTitle
) 
```

#### Parameters

*LowerBound*
:   Lower bound of range

*UpperBound*
:   Upper bound of range

*ProgressBarTitle*
:   Title of progress indicator to show in status bar

#### Return Value

True if progress indicator successfully started, false if not

Example

See the [IUserProgressBar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserProgressBar Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.md)  
[IUserProgressBar Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar_members.md)
