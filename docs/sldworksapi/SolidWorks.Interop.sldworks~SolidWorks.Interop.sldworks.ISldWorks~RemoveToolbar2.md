# RemoveToolbar2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveToolbar2`

Removes a toolbar created with ISldWorks::AddToolbar5.
Removes a toolbar created with [ISldWorks::AddToolbar5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveToolbar2( _
   ByVal Cookie As System.Integer, _
   ByVal ToolbarId As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim ToolbarId As System.Integer
Dim value As System.Boolean
 
value = instance.RemoveToolbar2(Cookie, ToolbarId)
```

```

System.bool RemoveToolbar2( 
   System.int Cookie,
   System.int ToolbarId
)
```

```

System.bool RemoveToolbar2( 
   System.int Cookie,
   System.int ToolbarId
) 
```

#### Parameters

*Cookie*
:   Resource ID of the toolbar; this is the same cookie that you specified in [ISwAddin::ConnectToSW](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.md)

*ToolbarId*
:   Toolbar ID

#### Return Value

True if the toolbar is removed, false if not

Remarks

If the SOLIDWORKS application is exiting and your application is still added-in, then you should not call this method. You should, however, clean up all other items such as the Cbitmap objects, which allows your toolbar to get reloaded in the same position next time you start the SOLIDWORKS application.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::DragToolbarButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton.md)  
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.md)
