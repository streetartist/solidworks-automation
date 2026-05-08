# ShowModelBreakState Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowModelBreakState`

Sets whether to display the specified Model Break View.
Sets whether to display the specified Model Break View.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ShowModelBreakState( _
   ByVal ShowIt As System.Boolean, _
   ByVal BreakName As System.String _
) As System.Boolean
```

```

Dim instance As IView
Dim ShowIt As System.Boolean
Dim BreakName As System.String
Dim value As System.Boolean
 
value = instance.ShowModelBreakState(ShowIt, BreakName)
```

```

System.bool ShowModelBreakState( 
   System.bool ShowIt,
   System.string BreakName
)
```

```

System.bool ShowModelBreakState( 
   System.bool ShowIt,
   System.String^ BreakName
) 
```

#### Parameters

*ShowIt*
:   True to display the Model Break View specified in BreakName, false to not

*BreakName*
:   Name of Model Break View to display

#### Return Value

True if successful, false if not

Example

[Get and Set Model Break View Display (VBA)](Get_and_Set_Model_Break_View_Display_Example_VB.htm)  
[Get and Set Model Break View Display (VB.NET)](Get_and_Set_Model_Break_View_Display_Example_VBNET.htm)  
[Get and Set Model Break View Display (C#)](Get_and_Set_Model_Break_View_Display_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::IsModelBreakState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelBreakState.md)
