# DocumentVisible Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DocumentVisible`

Allows the application to control the display of a document in a window upon creation or retrieval.
Allows the application to control the display of a document in a window upon creation or retrieval.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub DocumentVisible( _
   ByVal Visible As System.Boolean, _
   ByVal Type As System.Integer _
) 
```

```

Dim instance As ISldWorks
Dim Visible As System.Boolean
Dim Type As System.Integer
 
instance.DocumentVisible(Visible, Type)
```

```

void DocumentVisible( 
   System.bool Visible,
   System.int Type
)
```

```

void DocumentVisible( 
   System.bool Visible,
   System.int Type
) 
```

#### Parameters

*Visible*
:   True if the documents of the specified type are displayed upon creation or retrieval, false if not

*Type*
:   Type of document to which you apply visibility as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

Remarks

This method is a flag that allows you to display or hide documents as they are loaded.

If you create a document invisibly by passing false to this method, then you cannot make it visible with [IModelDoc2::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Visible.md). Instead you should close it and then reopen it as a visible document.

Additionally if SOLIDWORKS was hidden by a call to [ISldWorks::UserControlBackground](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControlBackground.md), and a document is opened (e.g., a configuration is loaded), then you must call this method to keep the SOLIDWORKS user interface hidden.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::UserControl Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControl.md)  
[ISldWorks::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.md)
