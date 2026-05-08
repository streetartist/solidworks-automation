# InitializeShading Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~InitializeShading`

Sets up the model view for OpenGL shading.
Sets up the model view for OpenGL shading.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InitializeShading() 
```

```

Dim instance As IModelView
 
instance.InitializeShading()
```

```

void InitializeShading()
```

```

void InitializeShading(); 
```

Remarks

Third-party developers should call this method if they are going to use OpenGL shading and are unsure whether shading has already been used for the current window. This method needs to be called for any window drawn into with OpenGL calls.

This method is provided so third-party applications do not need to use any of the Choos...() functions provided in the OpenGL library. Many of the Choos..() functions, for example ChoosePixelFormat(), can only be called once per window. In the case of ChoosePixelFormat(), a second call to the function is ignored. The effect is harmless if the third-party application makes this call after the SOLIDWORKS application has made the call. However, it is dangerous if the third party were to call it first because the SOLIDWORKS application may require a more complicated format.

To make OpenGL calls,you must get an OpenGL render context (RC). We keep our render context private so that there are not any problems with corruption of SOLIDWORKS RC by an application. To get a rendering context to make OpenGL calls, you must:

uiModelView\_c::InitializeShading()

CClientDC dC(CWnd\* parentWindow);

HGLRC hRc = ::wglCreateContext(dC.m\_hDC);

::wglMakeCurrent(dC.m\_hDC, hRc); (call this before each 'paint' operation)

When you are done using OpenGL for this paint'operation, call:

::wglMakeCurrent(NULL, NULL);

When the DLL shuts down or the [IModelView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md) object is destroyed (watch for a [DModelViewEvents DestroyNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_DestroyNotify2EventHandler.md)), your application must do the following:

::wglMakeCurrent(NULL, NULL);

::wglDeleteContext(hRc);

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelDoc2::ViewOglShading Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ViewOglShading.md)
