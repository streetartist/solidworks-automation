# IMirrorComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IMirrorComponents`

Obsolete. Superseded by IAssemblyDoc::MirrorComponents2.
Obsolete. Superseded by [IAssemblyDoc::MirrorComponents2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MirrorComponents2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IMirrorComponents( _
   ByVal Plane As System.Object, _
   ByVal InstanceCount As System.Integer, _
   ByRef ComponentsToInstance As Component2, _
   ByVal MirrorCount As System.Integer, _
   ByRef ComponentsToMirror As Component2, _
   ByVal NameCount As System.Integer, _
   ByRef MirroredComponentFilenames As System.String, _
   ByVal RecreateMates As System.Boolean, _
   ByVal ComponentModifier As System.Integer, _
   ByVal ComponentNameModifier As System.String, _
   ByVal MirroredFileLocation As System.String, _
   ByVal CopyCustomProperties As System.Boolean _
) As Component2
```

```

Dim instance As IAssemblyDoc
Dim Plane As System.Object
Dim InstanceCount As System.Integer
Dim ComponentsToInstance As Component2
Dim MirrorCount As System.Integer
Dim ComponentsToMirror As Component2
Dim NameCount As System.Integer
Dim MirroredComponentFilenames As System.String
Dim RecreateMates As System.Boolean
Dim ComponentModifier As System.Integer
Dim ComponentNameModifier As System.String
Dim MirroredFileLocation As System.String
Dim CopyCustomProperties As System.Boolean
Dim value As Component2
 
value = instance.IMirrorComponents(Plane, InstanceCount, ComponentsToInstance, MirrorCount, ComponentsToMirror, NameCount, MirroredComponentFilenames, RecreateMates, ComponentModifier, ComponentNameModifier, MirroredFileLocation, CopyCustomProperties)
```

```

Component2 IMirrorComponents( 
   System.object Plane,
   System.int InstanceCount,
   ref Component2 ComponentsToInstance,
   System.int MirrorCount,
   ref Component2 ComponentsToMirror,
   System.int NameCount,
   ref System.string MirroredComponentFilenames,
   System.bool RecreateMates,
   System.int ComponentModifier,
   System.string ComponentNameModifier,
   System.string MirroredFileLocation,
   System.bool CopyCustomProperties
)
```

```

Component2^ IMirrorComponents( 
   System.Object^ Plane,
   System.int InstanceCount,
   Component2^% ComponentsToInstance,
   System.int MirrorCount,
   Component2^% ComponentsToMirror,
   System.int NameCount,
   System.String^% MirroredComponentFilenames,
   System.bool RecreateMates,
   System.int ComponentModifier,
   System.String^ ComponentNameModifier,
   System.String^ MirroredFileLocation,
   System.bool CopyCustomProperties
) 
```

#### Parameters

*Plane*
:   Plane or planar face about which to mirror the components

*InstanceCount*
:   Number of instances of the components to mirror

*ComponentsToInstance*
:   Array of instances of the [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) to mirror

*MirrorCount*
:   Number of components to mirror

*ComponentsToMirror*
:   Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) to mirror

*NameCount*
:   Number of filenames for the newly created mirrored assemblies or parts

*MirroredComponentFilenames*
:   Array of filenames for the newly created mirrored assemblies or parts

*RecreateMates*
:   True to preserve any mates between the selected components if more than one component is to be mirrored, false to not

*ComponentModifier*
:   Prefix or suffix for the newly mirrored components if MirroredComponentFilenames is not specified, as defined by [swMirrorComponentNameModifier\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMirrorComponentNameModifier_e.html)

*ComponentNameModifier*
:   String to add to the prefix or suffix of the name of the newly mirrored components if MirroredComponentFilenames is not specified

*MirroredFileLocation*
:   Name of the folder where to store the file of the newly created mirrored components

*CopyCustomProperties*
:   True to copy the custom properties from the selected components to the mirrored components, false to not

#### Return Value

- in-process, unmanaged C++: Pointer to an array of newly created [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::MirrorComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MirrorComponents.md)
