# DSldWorksEvents_ReferenceNotFoundNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ReferenceNotFoundNotifyEventHandler`

Notifies the user program before the SOLIDWORKS software displays a dialog box prompting the end-user to browse for the referenced file.
Notifies the user program before the SOLIDWORKS software displays a dialog box prompting the end-user to browse for the referenced file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_ReferenceNotFoundNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_ReferenceNotFoundNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_ReferenceNotFoundNotifyEventHandler( 
   System.string FileName
)
```

```

public delegate System.int DSldWorksEvents_ReferenceNotFoundNotifyEventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Path and filename of the referenced file

Remarks

Use this event with [ISldWorks::SetMissingReferencePathName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMissingReferencePathName.md). Returning S\_false from your event handler successfully replaces the specified fileName with the filename specified in the call to ISldWorks::SetMissingReferencePathName.

This event is generated when a document is opened and one of its dependencies is not found.

If developing a C++ application, use [swAppReferenceNotFoundNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Example

This code illustrates the proper use of this event:

HRESULT swAppEvents::AppReferenceNotFoundNotify (BSTR FileName)

{

static bool test = true;

TRACE( \_T(" TestbedEvents - SldWorks.swAppReferenceNotFoundNotify event fired\n"));

if( test)

{

LPSLDWORKS pSldWorks = NULL;

m\_lpObject->QueryInterface(IID\_ISldWorks, (void\*\*)&pSldWorks);

pSldWorks->SetMissingReferencePathName( FileName);

pSldWorks->Release();

return S\_false;

}

else

return S\_OK;

}

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_ReferenceNotFoundNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_ReferenceNotFoundNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
