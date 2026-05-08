# SetSaveFlag Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSaveFlag`

Flags the document as dirty.
Flags the document as dirty.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetSaveFlag() 
```

```

Dim instance As IModelDoc2
 
instance.SetSaveFlag()
```

```

void SetSaveFlag()
```

```

void SetSaveFlag(); 
```

Remarks

If the user tries to close the part, the Do you wish to save changes? dialog is displayed.

If SOLIDWORKS data has changed, this method marks the SOLIDWORKS document as dirty so that the end-user is prompted when attempting to close the document. You might want to use this method with applications that use [IModelDoc2::IGet3rdPartyStorage](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.md) to save stream data in SOLIDWORKS files.

If you have programmatically changed the SOLIDWORKS model, using this method is not necessary because the SOLIDWORKS document is flagged as dirty automatically.

Example

[Remove Textures from Assembly Components (VBA)](Remove_Textures_from_Assembly_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetSaveFlag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSaveFlag.md)
