# ShowToolbar2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowToolbar2`

Obsolete. Not superseded.
Obsolete. Not superseded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ShowToolbar2( _
   ByVal Cookie As System.Integer, _
   ByVal ToolbarId As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim ToolbarId As System.Integer
Dim value As System.Boolean
 
value = instance.ShowToolbar2(Cookie, ToolbarId)
```

```

System.bool ShowToolbar2( 
   System.int Cookie,
   System.int ToolbarId
)
```

```

System.bool ShowToolbar2( 
   System.int Cookie,
   System.int ToolbarId
) 
```

#### Parameters

*Cookie*

*ToolbarId*

Remarks

SOLIDWORKS manages the display of the toolbars based on the user's action; therefore, this method is not needed. There are no alternative methods available to use.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
