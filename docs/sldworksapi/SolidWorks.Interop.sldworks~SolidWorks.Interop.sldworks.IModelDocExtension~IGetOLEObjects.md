# IGetOLEObjects Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetOLEObjects`

Get the OLE objects.
Get the OLE objects.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetOLEObjects( _
   ByVal Options As System.Integer, _
   ByVal OleObjectCount As System.Integer, _
   ByRef LpOleObjects As SwOLEObject _
) 
```

```

Dim instance As IModelDocExtension
Dim Options As System.Integer
Dim OleObjectCount As System.Integer
Dim LpOleObjects As SwOLEObject
 
instance.IGetOLEObjects(Options, OleObjectCount, LpOleObjects)
```

```

void IGetOLEObjects( 
   System.int Options,
   System.int OleObjectCount,
   out SwOLEObject LpOleObjects
)
```

```

void IGetOLEObjects( 
   System.int Options,
   System.int OleObjectCount,
   [Out] SwOLEObject^ LpOleObjects
) 
```

#### Parameters

*Options*
:   Options as defined in [swOleObjectOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOleObjectOptions_e.html)

*OleObjectCount*
:   Number of OLE objects

*LpOleObjects*
:   - in-process, unmanaged C++: Pointer to an array of the [OLE objects](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IModelDocExtension::GetOLEObjectCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjectCount.md) to determine the size of the output array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetOLEObjects Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetOLEObjects.md)
