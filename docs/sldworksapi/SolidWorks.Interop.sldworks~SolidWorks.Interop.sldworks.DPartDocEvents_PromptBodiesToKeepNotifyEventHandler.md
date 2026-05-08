# DPartDocEvents_PromptBodiesToKeepNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_PromptBodiesToKeepNotifyEventHandler`

Generated when a body is cut into multiple bodies.
Generated when a body is cut into multiple bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_PromptBodiesToKeepNotifyEventHandler( _
   ByVal Feature As System.Object, _
   ByRef Bodies As System.Object _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_PromptBodiesToKeepNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_PromptBodiesToKeepNotifyEventHandler( 
   System.object Feature,
   ref System.object Bodies
)
```

```

public delegate System.int DPartDocEvents_PromptBodiesToKeepNotifyEventHandler( 
   System.Object^ Feature,
   System.Object^% Bodies
)
```

#### Parameters

*Feature*
:   [Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

*Bodies*
:   Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

If developing a C++ application, use [swPartPromptBodiesToKeepNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Example

[Cut Body and Keep All Bodies (C#)](Cut_Body_and_Keep_All_Bodies_Example_CSharp.htm)  
[Cut Body and Keep All Bodies (VB.NET)](Cut_Body_and_Keep_All_Bodies_Example_VBNET.htm)  
[Cut Body and Keep All Bodies (VBA)](Cut_Body_and_Keep_All_Bodies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_PromptBodiesToKeepNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_PromptBodiesToKeepNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
