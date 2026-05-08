# GetUserProgressBar Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserProgressBar`

Gets a progress indicator.
Gets a progress indicator.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUserProgressBar( _
   ByRef PProgressBar As UserProgressBar _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim PProgressBar As UserProgressBar
Dim value As System.Boolean
 
value = instance.GetUserProgressBar(PProgressBar)
```

```

System.bool GetUserProgressBar( 
   out UserProgressBar PProgressBar
)
```

```

System.bool GetUserProgressBar( 
   [Out] UserProgressBar^ PProgressBar
) 
```

#### Parameters

*PProgressBar*
:   [IUserProgressBar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar.md)

#### Return Value

True if the progress indicator object is returned, false if not

Example

[Start, Update, and Stop Progress Indicator (VBA)](Start,_Update,_and_Stop_User_Progress_Indicator_Example_VB.htm)  
[Start, Update, and Stop Progress Indicator (VB.NET)](Start,_Update,_and_Stop_User_Progress_Bar_Example_VBNET.htm)  
[Start, Update, and Stop Progress Indicator (C#)](Start,_Update,_and_Stop_User_Progress_Bar_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[IStatusBarPane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane.md)
