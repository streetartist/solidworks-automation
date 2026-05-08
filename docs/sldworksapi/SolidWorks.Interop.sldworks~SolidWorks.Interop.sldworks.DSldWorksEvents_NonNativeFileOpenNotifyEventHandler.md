# DSldWorksEvents_NonNativeFileOpenNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_NonNativeFileOpenNotifyEventHandler`

Fired when non-native SOLIDWORKS files are opened.
Fired when non-native SOLIDWORKS files are opened.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_NonNativeFileOpenNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_NonNativeFileOpenNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_NonNativeFileOpenNotifyEventHandler( 
   System.string FileName
)
```

```

public delegate System.int DSldWorksEvents_NonNativeFileOpenNotifyEventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Name of the opened file

Remarks

This event occurs after automatic healing if it is enabled. To enable automatic healing, set swImportAutoRunImportDiagnosticsPersist and swImportAutoRunImportDiagnostics to True. See [swUserPreferenceToggle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceToggle_e.html), Import for details about these two enumerators.

The file types handled include files with these extensions: .dxf, .dwg, .igs, .sat, .step, .vda, .wrl, and .dll.

On receiving this event, you can call [ISldWorks::ActiveDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.md) or [ISldWorks::IActiveDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.md) to get the active [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) pointer.

In an environment when multiple applications are simultaneously loaded and have access to the SOLIDWORKS application through its APIs, exercise caution when this notification is processed. The active IModelDoc2 may not be the one that corresponds to the FileName argument. For example, this can occur when one of the translator DLL's receives this event and picks up the non-native file and generates a new SOLIDWORKS document. This could happen prior to your application receiving this event.

 If developing a C++ application, use [swAppNonNativeFileOpenNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_NonNativeFileOpenNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_NonNativeFileOpenNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
