# ReloadWithReferences Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReloadWithReferences`

Reloads this model document with the specified references.
Reloads this model document with the specified references.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReloadWithReferences( _
   ByVal ReadOnly As System.Boolean, _
   ByVal DiscardChanges As System.Boolean, _
   ByVal ReferencesToReload As System.Object _
) As System.Integer
```

```

Dim instance As IModelDocExtension
Dim ReadOnly As System.Boolean
Dim DiscardChanges As System.Boolean
Dim ReferencesToReload As System.Object
Dim value As System.Integer
 
value = instance.ReloadWithReferences(ReadOnly, DiscardChanges, ReferencesToReload)
```

```

System.int ReloadWithReferences( 
   System.bool ReadOnly,
   System.bool DiscardChanges,
   System.object ReferencesToReload
)
```

```

System.int ReloadWithReferences( 
   System.bool ReadOnly,
   System.bool DiscardChanges,
   System.Object^ ReferencesToReload
) 
```

#### Parameters

*ReadOnly*
:   True to set the model document read-only after reload or replace, false to allow write access

*DiscardChanges*
:   True to discard changes made to the current model document, false to abort operation if the model document was changed (see **Remarks**)

*ReferencesToReload*
:   Array of IDispatch pointers to referenced documents to reload

#### Return Value

Error codes as defined by [swComponentReloadError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentReloadError_e.html)

Remarks

The model to reload or replace must be open in its own window frame.

This method:

- provides a performance improvement over [IModelDocExtension::ReloadOrReplace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReloadOrReplace.md) (when its ForceReload parameter is set to True).

- is faster because it reloads only a selection of referenced components.
- does not reload or replace the model if the top assembly has been opened invisibly. In that case, make the model visible by calling [IModelDoc2::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Visible.md) before calling this method.
- must be called after calling [IModelDoc2::ForceReleaseLocks](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceReleaseLocks.md), which detaches a file from the file system, to re-attach a detached file to the file system. If you do not call this method after calling IModelDoc2::ForceReleaseLocks, then you will experience problems with OLE objects (e.g., design tables). Any changes made to a file while it is detached are not preserved unless you save the file to disk before calling this method. Additionally if you set this method's DiscardChanges parameter to false and you made changes to a detached file that you are attempting to re-attach to the file system, then this method will fail. DiscardChanges must be set to true to re-attach a detached file.

See [ISldWorks::CloseAndReopen](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAndReopen.md) to perform a similar function with drawing documents.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
