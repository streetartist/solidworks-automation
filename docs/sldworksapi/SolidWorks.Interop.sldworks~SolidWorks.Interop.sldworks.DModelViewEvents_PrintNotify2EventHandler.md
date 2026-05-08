# DModelViewEvents_PrintNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_PrintNotify2EventHandler`

Notifies the user program when a document is printed.
Notifies the user program when a document is printed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DModelViewEvents_PrintNotify2EventHandler( _
   ByVal pDC As System.Long, _
   ByVal bPreview As System.Boolean _
) As System.Integer
```

```

Dim instance As New DModelViewEvents_PrintNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DModelViewEvents_PrintNotify2EventHandler( 
   System.long pDC,
   System.bool bPreview
)
```

```

public delegate System.int DModelViewEvents_PrintNotify2EventHandler( 
   System.int64 pDC,
   System.bool bPreview
)
```

#### Parameters

*pDC*
:   Pointer to the printer device context used to print the document (**see Remarks**)

*bPreview*
:   True to preview the document, false to not

Remarks

Always return S\_OK in the swViewPrintNotify2 event handler.

If developing a C++ application, use [swViewPrintNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

pDC is the address of an MFC CDC instance, and it can be cast to a CDC\*. C++ applications wanting to use this CDC\* need to dynamically link to the MFC DLLs and use the same version of the Visual C++ compiler that SOLIDWORKS uses.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DModelViewEvents\_PrintNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_PrintNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
