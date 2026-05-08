# GetNext Method (IDatumOrigin)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~GetNext`

Gets the next datum origin in the view.
Gets the next datum origin in the view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNext() As DatumOrigin
```

```

Dim instance As IDatumOrigin
Dim value As DatumOrigin
 
value = instance.GetNext()
```

```

DatumOrigin GetNext()
```

```

DatumOrigin^ GetNext(); 
```

#### Return Value

Pointer to the [datum origin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.md) in the view

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.md)  
[IDatumOrigin Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.md)  
[IView::GetFirstDatumOrigin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDatumOrigin.md)  
[IAnnotation::GetSpecificAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetSpecificAnnotation.md)  
[IAnnotation::IGetSpecificAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetSpecificAnnotation.md)  
[IHoleTable::DatumOrigin Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~DatumOrigin.md)
