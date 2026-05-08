# PreviewDoc Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreviewDoc`

Displays a preview of a document to the specified window.
Displays a preview of a document to the specified window.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PreviewDoc( _
   ByRef HWnd As System.Integer, _
   ByVal FullName As System.String _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim HWnd As System.Integer
Dim FullName As System.String
Dim value As System.Boolean
 
value = instance.PreviewDoc(HWnd, FullName)
```

```

System.bool PreviewDoc( 
   ref System.int HWnd,
   System.string FullName
)
```

```

System.bool PreviewDoc( 
   System.int% HWnd,
   System.String^ FullName
) 
```

#### Parameters

*HWnd*
:   Window handle where you want the preview bitmap to display; this pointer is not valid across processes; therefore, this method only works if your application is implemented as a DLL

*FullName*
:   Full path name of document to preview

#### Return Value

True if successful, false if not

Remarks

If your application must be x64 compatible, then use [ISldWorks::PreviewDocx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreviewDocx64.md).

The bitmap is stored with the fixed size shown with the interactive SOLIDWORKS preview option. If your window is a different size, then the image is scaled appropriately. If scaling is needed, then shaded images may not be as crisp as the original.

This method works well in the WM\_PAINT Windows Message handler. If used in WM\_ONINITDIALOG the dialog only displays the preview for a brief moment. The reason is that the dialog should be initialized completely before calling SldWorks::PreviewDoc.

C++ programmers can also access this bitmap image from outside SOLIDWORKS. The bitmap was written with CArchive::Write( ) and is found in the Preview node in SOLIDWORKS part, assembly and drawing files. The format of the Preview node is as follows: DWORD (data size) followed by continues chunk of memory of that size (data). The data being read can be cast to LPBITMAPINFO, which has all of the information required to display the bitmap. You may want to use StretchDIBits() when displaying your image of the bitmap.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::OpenDoc6 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md)  
[ISldWorks::GetPreviewBitmap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetPreviewBitmap.md)
