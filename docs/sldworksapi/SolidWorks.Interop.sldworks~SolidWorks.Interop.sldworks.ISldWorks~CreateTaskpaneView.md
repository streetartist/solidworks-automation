# CreateTaskpaneView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView`

Obsolete. Superseded by ISldworks::CreateTaskpaneView2.
Obsolete. Superseded by [ISldworks::CreateTaskpaneView2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateTaskpaneView( _
   ByRef Bitmap As System.Integer, _
   ByVal ToolTip As System.String, _
   ByVal PHandler As System.Object _
) As TaskpaneView
```

```

Dim instance As ISldWorks
Dim Bitmap As System.Integer
Dim ToolTip As System.String
Dim PHandler As System.Object
Dim value As TaskpaneView
 
value = instance.CreateTaskpaneView(Bitmap, ToolTip, PHandler)
```

```

TaskpaneView CreateTaskpaneView( 
   ref System.int Bitmap,
   System.string ToolTip,
   System.object PHandler
)
```

```

TaskpaneView^ CreateTaskpaneView( 
   System.int% Bitmap,
   System.String^ ToolTip,
   System.Object^ PHandler
) 
```

#### Parameters

*Bitmap*

*ToolTip*

*PHandler*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
