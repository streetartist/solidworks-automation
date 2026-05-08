# ReloadOrReplace Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ReloadOrReplace`

Obsolete. Superseded by IModelDocExtension::ReloadOrReplace.
Obsolete. Superseded by [IModelDocExtension::ReloadOrReplace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReloadOrReplace.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReloadOrReplace( _
   ByVal ReadOnly As System.Boolean, _
   ByVal ReplaceFileName As System.String, _
   ByVal DiscardChanges As System.Boolean _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim ReadOnly As System.Boolean
Dim ReplaceFileName As System.String
Dim DiscardChanges As System.Boolean
Dim value As System.Integer
 
value = instance.ReloadOrReplace(ReadOnly, ReplaceFileName, DiscardChanges)
```

```

System.int ReloadOrReplace( 
   System.bool ReadOnly,
   System.string ReplaceFileName,
   System.bool DiscardChanges
)
```

```

System.int ReloadOrReplace( 
   System.bool ReadOnly,
   System.String^ ReplaceFileName,
   System.bool DiscardChanges
) 
```

#### Parameters

*ReadOnly*
:   True to set the model document read-only after reload or replace, false to allow write access

*ReplaceFileName*
:   Replacement model document; null or Nothing to reload the current model document

*DiscardChanges*
:   True to discard changes made to the current model document, false to abort operation if the model document was changed (see **Remarks**)

#### Return Value

Error codes as defined by [swComponentReloadError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentReloadError_e.html)

Remarks

The model to reload or replace must be open in its own window frame.

 

This method does not reload or replace the model if the top assembly has been opened invisibly. In that case, make the model visible by calling [IModelDoc2::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Visible.md) before calling this method.

You must call IModelDoc2::ReloadOrReplace after calling [IModelDoc2::ForceReleaseLocks](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceReleaseLocks.md), which detaches a file from the file system, to re-attach a detached file to the file system. If you do not call IModelDoc2::ReloadOrReplace after calling IModelDoc2::ForceReleaseLocks, then you will experience problems with OLE objects (e.g., design tables). Any changes made to a file while it is detached are not preserved unless you save the file to disk before calling IModelDoc2::ReloadOrReplace. Additionally if you set IModelDoc2::ReloadOrReplace's DiscardChanges parameter to false and you made changes to a detached file that you are attempting to re-attach to the file system, then IModelDoc2::ReloadOrReplace will fail. DiscardChanges must be set to true to re-attach a detached file.

See [ISldWorks::CloseAndReopen](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAndReopen.md) to perform a similar function with drawing documents.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IAssemblyDoc::ReplaceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents.md)  
[IAssemblyDoc::ComponentReload2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ComponentReload2.md)
