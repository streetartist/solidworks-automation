# InsertPart Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertPart`

Obsolete. Superseded by IPartDoc::InsertPart2.
Obsolete. Superseded by [IPartDoc::InsertPart2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertPart2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertPart( _
   ByVal FileName As System.String, _
   ByVal ImportPlane As System.Boolean, _
   ByVal ImportAxis As System.Boolean, _
   ByVal ImportCThread As System.Boolean _
) As Feature
```

```

Dim instance As IPartDoc
Dim FileName As System.String
Dim ImportPlane As System.Boolean
Dim ImportAxis As System.Boolean
Dim ImportCThread As System.Boolean
Dim value As Feature
 
value = instance.InsertPart(FileName, ImportPlane, ImportAxis, ImportCThread)
```

```

Feature InsertPart( 
   System.string FileName,
   System.bool ImportPlane,
   System.bool ImportAxis,
   System.bool ImportCThread
)
```

```

Feature^ InsertPart( 
   System.String^ FileName,
   System.bool ImportPlane,
   System.bool ImportAxis,
   System.bool ImportCThread
) 
```

#### Parameters

*FileName*
:   Name of part file

*ImportPlane*
:   True if the planes from the part should be imported into this part, false if not

*ImportAxis*
:   True if the axes from the part should be imported into this part, false if not

*ImportCThread*
:   True if the cosmetic threads from the part should be imported into this part, false if not

#### Return Value

New [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

This method inserts the specified part at the origin of this part. To position the insert part at a different location or orientation or both, use [IFeatureManager::InsertMoveCopyBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveCopyBody2.md).

The interface returned by this method is [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md), which gives you access to the feature APIs such as [IFeature::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.md) to get or set the name of the feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)
